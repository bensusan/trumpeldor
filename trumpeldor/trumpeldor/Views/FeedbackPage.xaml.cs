using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class FeedbackPage : ContentPage
	{
        GameController gc;
        int numberOfInnerGrids = 0;
        public FeedbackPage ()
		{
			InitializeComponent();
            gc = GameController.getInstance();
            AddFeedbacks();
        }

        private void AddFeedbacks()
        {
            List<FeedbackInstance> tripFeedbacks = gc.currentTrip.feedbacks;
            foreach (FeedbackInstance fi in tripFeedbacks)
                AddFeedback(fi);
        }

        private void AddFeedback(FeedbackInstance fi)
        {
            int nextRow = feedbacks.RowDefinitions.Count;
            nextRow += 2*numberOfInnerGrids;
            feedbacks.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            Label lbl = new Label { Text = gc.GetCurrentLanguageText(fi.feedback.question), HorizontalOptions = LayoutOptions.CenterAndExpand };
            lbl.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
            feedbacks.Children.Add(lbl, 0, nextRow);
            Feedback.Kinds kind;
            Feedback.kindToEnum.TryGetValue(fi.feedback.kind, out kind);
            Entry entry = null;
            if (kind == Feedback.Kinds.FeedBackText)
            {
                entry = new Entry { Keyboard = Keyboard.Text };
                if (fi.answer != null)
                    entry.Text = fi.answer;
                feedbacks.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
                entry.SetDynamicResource(VisualElement.StyleProperty, "entryStyle");
                feedbacks.Children.Add(entry, 0, nextRow + 1);
            }
            else if (kind == Feedback.Kinds.FeedBackRating)
            {
                Grid rateGrid = new Grid();
                rateGrid.SetDynamicResource(VisualElement.StyleProperty, "gridStyle");
                for (int i = 0; i < 5; i++)
                {
                    Label num = new Label { Text = (i+1) + "" , HorizontalOptions = LayoutOptions.CenterAndExpand };
                    num.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                    rateGrid.Children.Add(num, i, 0);
                    ImageButton button = new ImageButton { Source = ServerConection.URL_MEDIA + (i+1) + ".jpg", HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = Color.White };
                    button.Clicked += (sender, e) =>
                    {
                        int numberOfChildren = rateGrid.Children.Count;
                        for (int childIndex = 0; childIndex < numberOfChildren; ++childIndex){
                            //var column = Grid.GetColumn(rateGrid.Children[childIndex]);
                            if(Grid.GetRow(rateGrid.Children[childIndex]) == 1)
                            {
                                ImageButton ib = (ImageButton)rateGrid.Children[childIndex];
                                ib.BorderColor = feedbacks.BackgroundColor;
                                ib.BorderWidth = 0;
                            }
                        }
                        ImageButton clickedBtn = ((ImageButton)sender);
                        clickedBtn.BorderColor = Color.Black;
                        clickedBtn.BorderWidth = 1;
                    };
                    button.SetDynamicResource(VisualElement.StyleProperty, "regularCircleImageButtonStyle");

                    if (fi.answer != null && fi.answer.Equals((i + 1) + ""))
                    {
                        button.BorderColor = Color.Black;
                        button.BorderWidth = 1;
                    }
                    rateGrid.Children.Add(button, i, 1);
                }
                feedbacks.Children.Add(rateGrid, 0, nextRow + 1);
                numberOfInnerGrids ++;
            }
        }

        private void Reply_Button_Clicked(object sender, EventArgs e)
        {
            int indexFeedback = 0;
            foreach (View child in feedbacks.Children)
            {
                if (child is Entry)
                {
                    gc.currentTrip.feedbacks[indexFeedback].answer = ((Entry)child).Text;
                    indexFeedback++;
                }
                else if(child is Grid)
                {
                    Grid ch = ((Grid)child);
                    int numberOfChildren = ch.Children.Count;
                    for (int childIndex = 0; childIndex < numberOfChildren; ++childIndex)
                    {
                        //var column = Grid.GetColumn(rateGrid.Children[childIndex]);
                        if (Grid.GetRow(ch.Children[childIndex]) == 1)
                        {
                            ImageButton ib = (ImageButton)ch.Children[childIndex];
                            if (ib.BorderWidth != 0)
                                gc.currentTrip.feedbacks[indexFeedback].answer = (Grid.GetColumn(ch.Children[childIndex]) + 1) + "";
                        }
                    }
                    indexFeedback++;
                    //counter++;
                    //ImageButton ib = (ImageButton)child;
                    //if (ib.BorderWidth != 0)
                    //{
                    //    gc.currentTrip.feedbacks[indexFeedback].answer = (Grid.GetColumn(child) + 1) + "";
                    //    indexFeedback++;
                    //    lastAnswerRow = Grid.GetRow(child);
                    //    counter = 0;
                    //}
                    //if(counter == 5)
                    //    indexFeedback++;
                }
            }
            gc.UpdateTrip();

            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new FirstPage();
        }
    }
}