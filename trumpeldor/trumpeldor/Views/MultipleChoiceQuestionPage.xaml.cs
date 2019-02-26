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
	public partial class MultipleChoiceQuestionPage : ContentPage
	{
        GameController gc;
        private AmericanQuestion aq;
        public MultipleChoiceQuestionPage (AmericanQuestion aq)
		{
			InitializeComponent ();
            this.aq = aq;
            gc = GameController.getInstance();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            attractionQuestion.Text = aq.question;
            answersInitialize();
        }
        private void answersInitialize()
        {
            for (int i = 0; i < aq.answers.Count; i++)
            {
                Button answerButton = new Button();
                answerButton.Text = aq.answers.ElementAt(i);
                answerButton.Style = (Style)Application.Current.Resources["largeButtonStyle"];
                if (i == aq.indexOfCorrectAnswer)
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
        private async void Correct_Answer_Button_Clicked(object sender, EventArgs e)
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
            await DisplayAlert(AppResources.Destionation_Complete, "", AppResources.ok);
            await gc.FinishAttraction();
            if (gc.isFinishTrip)
            {
                Application.Current.MainPage = new FinishTrackPage(await gc.CanContinueToLongerTrack());
            }
            else
            {
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