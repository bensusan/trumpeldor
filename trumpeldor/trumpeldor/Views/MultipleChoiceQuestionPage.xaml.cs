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
		public MultipleChoiceQuestionPage ()
		{
			InitializeComponent ();
            scoreLabel.Text = "score: " + ((App)Application.Current).getGameController().getScore();
            trackPointQuestion.Text = ((App)Application.Current).getGameController().getCurrentTrackPointQuestion();
            if (((App)(Application.Current)).getGameController().isCurrentTrackPointHasQuestionImage())
            {
                trackPointQuestionImage.IsVisible = true;
                trackPointQuestionImage.Source = ((App)Application.Current).getGameController().getCurrentTrackPointQuestionImage();
            }
            else
            {
                trackPointQuestionImage.IsVisible = false;
            }
            answersInitialize();
        }
        private void answersInitialize()
        {
            List<String> answers = ((App)(Application.Current)).getGameController().getCurrentTrackPointQuestionAnswers();
            int correctAnswer = ((App)(Application.Current)).getGameController().getCurrentTrackPointCurrectAnswersToQuestion();
            for (int i = 0; i < answers.Count; i++)
            {
                Button answerButton = new Button();
                answerButton.Text = answers.ElementAt(i);
                answerButton.Style = (Style)Application.Current.Resources["buttonStyle"];
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
                answer.Style = (Style)Application.Current.Resources["buttonStyle"];
            }
            ((Button)sender).BackgroundColor = Color.Green;
            if(((App)Application.Current).getGameController().isFinishTrack())
            {
                Application.Current.MainPage = new FinishTrackPage();
            }
            else
            {
                ((App)Application.Current).getGameController().selectNextTrackPoint();
                Application.Current.MainPage = new NavigationPage();
            }

        }
        private void Wrong_Answer_Button_Clicked(object sender, EventArgs e)
        {
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["buttonStyle"];
            }
            ((Button)sender).BackgroundColor = Color.Red;
        }

        private void returnButton_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new TrackPointPage();
        }
    }
}