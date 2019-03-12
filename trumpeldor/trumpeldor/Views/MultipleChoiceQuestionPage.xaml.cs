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
        private static int DESIRED_SECONDS_TO_WAIT = 5;

        bool doneWaiting = false;
        int numOfSecondsLeft = 5;

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
        private async void Wrong_Answer_Button_Clicked(object sender, EventArgs e)
        {
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.AQ_Mistake);
            foreach (Button answer in answersLayout.Children)
            {
                answer.BackgroundColor = Color.Default;
                answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            }
            ((Button)sender).BackgroundColor = Color.Red;
            mistakes += 1;
            if (mistakes >= DESIRED_MISTAKES)
            {
                await DisplayAlert(
                    AppResources.Too_Much_Mistakes_In_AQ_title,
                    AppResources.Too_Much_Mistakes_In_AQ_Message_Part1
                    + " " + DESIRED_MISTAKES + " "
                    + AppResources.Too_Much_Mistakes_In_AQ_Message_Part2
                    + " " + DESIRED_SECONDS_TO_WAIT + " "
                    + AppResources.Too_Much_Mistakes_In_AQ_Message_Part3,
                    AppResources.ok);

                //Device.StartTimer(TimeSpan.FromSeconds(1), () => callBack());
                //while (!doneWaiting) ;
                //doneWaiting = false;
                for (int i = 0; i < DESIRED_SECONDS_TO_WAIT; i++)
                {
                    //await DisplayAlert("" + i, "", AppResources.ok);
                    var t = Task.Delay(1000);
                    t.Wait();
                }
                await DisplayAlert("You are good to go", "", AppResources.ok);
            }
        }
        
        bool callBack()
        {
            Device.BeginInvokeOnMainThread(() => DisplayAlert("" + numOfSecondsLeft, "", AppResources.ok));
            if (numOfSecondsLeft == 1)
            {
                numOfSecondsLeft = 5;
                doneWaiting = true;
                return false;
            }
            numOfSecondsLeft--;
            return true;
        }
    }
}