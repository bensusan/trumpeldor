using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class MultipleChoiceQuestionPage : ContentPage
	{
        GameController gc = ((App)Application.Current).getGameController();

        public MultipleChoiceQuestionPage ()
		{
			InitializeComponent ();
            scoreLabel.Text = "score: " + gc.GetScore();
            attractionQuestion.Text = gc.GetCurrentAttractionQuestion();
            if (gc.IsCurrentAttractionHasQuestionImage())
            {
                attractionQuestionImage.IsVisible = true;
                attractionQuestionImage.Source = gc.GetCurrentAttractionQuestionImage();
            }
            else
            {
                attractionQuestionImage.IsVisible = false;
            }
            answersInitialize();
        }
        private void answersInitialize()
        {
            List<String> answers = gc.GetCurrentAttractionQuestionAnswers();
            int correctAnswer = gc.GetCurrentAttractionCurrectAnswersToQuestion();
            for (int i = 0; i < answers.Count; i++)
            {
                Button answerButton = new Button();
                answerButton.Text = answers.ElementAt(i);
                answerButton.Style = (Style)Application.Current.Resources["largeButtonStyle"];
                if (i == correctAnswer)
                {
                    answerButton.Clicked += Correct_Answer_Button_Clicked;
                }
                else
                {
                    answerButton.Clicked += Wrong_Answer_Button_Clicked;
                }
                answersLayout.Children.Add(answerButton);
            }
        }
        private void Correct_Answer_Button_Clicked(object sender, EventArgs e)
        {
            
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            }

            ((Button)sender).BackgroundColor = Color.Green;
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            if (gc.isFinishTrip)
            {
                Application.Current.MainPage = new FinishTrackPage();
            }
            else
            {
                ((App)Application.Current).getGameController().SelectNextAttraction();
                Application.Current.MainPage = new NavigationPage();
            }

        }
        private void Wrong_Answer_Button_Clicked(object sender, EventArgs e)
        {
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            }
            ((Button)sender).BackgroundColor = Color.Red;
        }


        private void returnButton_Clicked(object sender, EventArgs e)
        {
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new AttractionPage();
        }
    }
}