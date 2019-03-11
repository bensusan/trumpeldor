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
        private int mistakes;
        private static int DESIRED_MISTAKES = 2;

        public MultipleChoiceQuestionPage (AmericanQuestion aq)
		{
			InitializeComponent ();
            this.mistakes = 0;
            this.aq = aq;
            gc = GameController.getInstance();
            attractionQuestion.Text = aq.question;
            answersInitialize();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
        }

        private static Random rng = new Random();

        public static int Shuffle(IList<string> list, int correctAnswerIndex)
        {
            int ans = correctAnswerIndex;
            int n = list.Count;
            while (n > 1)
            {
                n--;
                int k = rng.Next(n + 1);
                string value = list[k];
                list[k] = list[n];
                list[n] = value;
                if (ans == k)
                    ans = n;
                else if (ans == n)
                    ans = k;
            }
            return ans;
        }

        private void answersInitialize()
        {
            List<string> answers = new List<string>(aq.answers);
            int correctAnswerIndex = Shuffle(answers, aq.indexOfCorrectAnswer);
            for (int i = 0; i < answers.Count; i++)
            {
                Button answerButton = new Button();
                answerButton.Text = answers.ElementAt(i);
                answerButton.Style = (Style)Application.Current.Resources["largeButtonStyle"];
                if (i == correctAnswerIndex)
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
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.AQ_Correct);
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            }

            ((Button)sender).BackgroundColor = Color.Green;
            Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.Destionation_Complete, "", AppResources.ok));
            gc.FinishAttraction();

            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            if (gc.isFinishTrip)
            {
                Application.Current.MainPage = new FinishTrackPage(gc.CanContinueToLongerTrack());
            }
            else
            {
                Application.Current.MainPage = new NavigationPage();
            }

        }
        private void Wrong_Answer_Button_Clicked(object sender, EventArgs e)
        {
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.AQ_Mistake);
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            }
            ((Button)sender).BackgroundColor = Color.Red;
            mistakes += 1;
            if(mistakes >= DESIRED_MISTAKES)
                Device.BeginInvokeOnMainThread(async() => await Task.Delay(5000));
        }
    }
}