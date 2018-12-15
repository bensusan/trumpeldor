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
	public partial class FinishTrackPage : ContentPage
	{
		public FinishTrackPage ()
		{
			InitializeComponent ();
            titleLabel.Text = "congratulation you finish the track with " + ((App)Application.Current).getGameController().GetScore() + " points.";
            if (!((App)Application.Current).getGameController().CanContinueToLongerTrack())
            {
                continueButton.IsVisible = false;
            }

        }

        private void Continiue_Button_Clicked(object sender, EventArgs e)
        {
            ((App)Application.Current).getGameController().ContinueToLongerTrack();
            ((App)Application.Current).getGameController().SelectNextTrackPoint();

            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new NavigationPage(); 
        }
        private void Share_Button_Clicked(object sender, EventArgs e)
        {

        }
        private void Leading_Table_Button_Clicked(object sender, EventArgs e)
        {

        }
        private async void feedback_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new FeedbackPage());
        }
        private async void information_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage());
        }
    }
}