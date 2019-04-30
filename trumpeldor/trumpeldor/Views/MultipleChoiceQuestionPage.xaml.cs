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

        public MultipleChoiceQuestionPage ()
		{
			InitializeComponent ();
            this.mistakes = 0;
            gc = GameController.getInstance();
            this.aq = gc.currentTrip.GetCurrentAttraction().americanQuestion;
            attractionQuestion.Text = aq.question;
            answersInitialize();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
        }

        private static Random rng = new Random();

        public static int[] Shuffle(IList<string> list, int[] correctAnswerIndex)
        {
            int[] ans = new int[correctAnswerIndex.Length];
            correctAnswerIndex.CopyTo(ans, 0);
            int n = list.Count;
            while (n > 1)
            {
                n--;
                int k = rng.Next(n + 1);
                string value = list[k];
                list[k] = list[n];
                list[n] = value;
                for(int i = 0; i < ans.Length; i++){
                    if (ans[i] == k)
                        ans[i] = n;
                    else if (ans[i] == n)
                        ans[i] = k;
                }
            }
            return ans;
        }

        private void answersInitialize()
        {
            List<string> answers = new List<string>(aq.answers);
            int[] correctAnswerIndex = Shuffle(answers, aq.indexOfCorrectAnswer); //TODO change to all correct indexes
            for (int i = 0; i < answers.Count; i++)
            {
                Button answerButton = new Button();
                answerButton.Text = answers.ElementAt(i);
                answerButton.Style = (Style)Application.Current.Resources["largeButtonStyle"];
                bool isFound = false;
                for(int j= 0; j<correctAnswerIndex.Length; j++){
                    if (i == correctAnswerIndex[j]){
                        isFound = true;
                        break;
                    }
                }
                if (isFound)
                    answerButton.Clicked += Correct_Answer_Button_Clicked;
                else
                    answerButton.Clicked += Wrong_Answer_Button_Clicked;
                answersLayout.Children.Add(answerButton);
            }
        }
        private async void Correct_Answer_Button_Clicked(object sender, EventArgs e)
        {
            //foreach (Button answer in answersLayout.Children)
            //    answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            ((Button)sender).BackgroundColor = Color.Green;
            await Task.Delay(100);
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.AQ_Correct);
            gc.FinishAttraction();

            await Navigation.PopModalAsync();
        }
        private async void Wrong_Answer_Button_Clicked(object sender, EventArgs e)
        {
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.AQ_Mistake);
            //foreach (Button answer in answersLayout.Children)
            //    answer.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            Color regular = ((Button)sender).BackgroundColor;
            ((Button)sender).BackgroundColor = Color.Red;
            await Task.Delay(50);
            mistakes += 1;
            if (mistakes >= DESIRED_MISTAKES)
            {
                //await DisplayAlert(
                //    AppResources.Too_Much_Mistakes_In_AQ_title,
                //    AppResources.Too_Much_Mistakes_In_AQ_Message_Part1
                //    + " " + DESIRED_MISTAKES + " "
                //    + AppResources.Too_Much_Mistakes_In_AQ_Message_Part2
                //    + " " + DESIRED_SECONDS_TO_WAIT + " "
                //    + AppResources.Too_Much_Mistakes_In_AQ_Message_Part3,
                //    AppResources.ok);

                explanation.IsVisible = true;
                numToWait.IsVisible = true;
                for (int i = DESIRED_SECONDS_TO_WAIT; i >= 0; i--){
                    numToWait.Text = i + "";
                    await Task.Delay(1000);
                }
                numToWait.IsVisible = false;
                explanation.IsVisible = false;
            }
            else
                await Task.Delay(100);
            ((Button)sender).BackgroundColor = regular;
        }
    }
}