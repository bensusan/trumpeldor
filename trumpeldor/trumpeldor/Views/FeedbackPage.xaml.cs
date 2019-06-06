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
            feedbacks.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            Label lbl = new Label { Text = fi.feedback.question, HorizontalOptions = LayoutOptions.CenterAndExpand };
            lbl.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
            feedbacks.Children.Add(lbl, 0, nextRow);
            Feedback.Kinds kind;
            Feedback.kindToEnum.TryGetValue(fi.feedback.kind, out kind);
            Entry entry = null;
            if (kind == Feedback.Kinds.FeedBackText)
                entry = new Entry { Keyboard = Keyboard.Text }; 
            else if (kind == Feedback.Kinds.FeedBackRating)
                entry = new Entry { Keyboard = Keyboard.Numeric };  //TODO - change to stars according to link
            if (fi.answer != null)
                entry.Text = fi.answer;
            feedbacks.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            entry.SetDynamicResource(VisualElement.StyleProperty, "entryStyle");
            feedbacks.Children.Add(entry, 0, nextRow+1);
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