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
            titleLabel.Text = "congratulation you finish the track with " + ((App)Application.Current).getGameController().GetScore() + " points";
            if (!((App)Application.Current).getGameController().CanContinueToLongerTrack())
            {
                continueButton.IsVisible = false;
            }

        }

        private void Continiue_Button_Clicked(object sender, EventArgs e)
        {
            ((App)Application.Current).getGameController().ContinueToLongerTrack();
            ((App)Application.Current).getGameController().SelectNextTrackPoint();
            Application.Current.MainPage = new NavigationPage();
        }
        private void Share_Button_Clicked(object sender, EventArgs e)
        {

        }
        private void Leading_Table_Button_Clicked(object sender, EventArgs e)
        {

        }
        private void feedback_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new FeedbackPage();
        }
        private void information_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new informationPage();
        }
    }
}