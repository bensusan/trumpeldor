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
	public partial class AttractionPage : ContentPage
	{
        private GameController gc;
        private Attraction attraction;
        private bool isFirstAppear;
        public AttractionPage()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            this.attraction = gc.currentTrip.GetCurrentAttraction();
            attractionName.Text = this.attraction.name;
            string mainPictureUrl = this.attraction.GetMainPictureUrl();
            attractionImage.Source = mainPictureUrl;
            attractionImage.IsVisible = !mainPictureUrl.Equals("");
            watchAgainButton.IsVisible = !this.attraction.GetARURL().Equals("");            
            isFirstAppear = true;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            missionButton.IsEnabled = !gc.isAttractionDone;
            continueButton.IsEnabled = gc.isAttractionDone;
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            if (isFirstAppear)
            {
                DependencyService.Get<IAudioService>().PlayAudioFile("TaDa.mp3");
                isFirstAppear = false;
            }
        }

        private async void Information_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage(this.attraction));
        }

        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MissionPage(this));
        }

        private void Watch_Again_Button_Clicked(object sender, EventArgs e)
        {
            //TODO
        }

        private void Continue_Button_Clicked(object sender, EventArgs e)
        {
            gc.isAttractionDone = false;
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


    }
}