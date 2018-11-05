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
	public partial class TrackPointPage : ContentPage
	{
		public TrackPointPage ()
		{
			InitializeComponent ();
            scoreLabel.Text = "score: " + ((App)Application.Current).getGameController().getScore();
            trackPointName.Text = ((App)Application.Current).getGameController().getCurrentTrackPointName();
            if (((App)(Application.Current)).getGameController().isCurrentTrackPointHasImage()){
                trackPointImage.IsVisible = true;
                trackPointImage.Source = ((App)Application.Current).getGameController().getCurrentTrackPointImage();
            }
            else{
                trackPointImage.IsVisible = false;
            }

            if (((App)(Application.Current)).getGameController().isCurrentTrackPointHasAR()){
                watchAgainButton.IsVisible = true;
            }
            else{
                watchAgainButton.IsVisible = false;
            }
        }

        private void Information_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new TrackPointInformationPage();
        }
        private void Mission_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new MissionPage();
        }
        private void Question_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new MultipleChoiceQuestionPage();
        }
        private void Watch_Again_Button_Clicked(object sender, EventArgs e)
        {
            //TODO
        }
    }
}