using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
using System.IO;
using Rg.Plugins.Popup.Services;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class AttractionPage : ContentPage
	{
        private GameController gc;
        private Attraction attraction;
        private bool isFirstAppear;
        private Entertainment entertainment = null;
        public AttractionPage()
		{
			InitializeComponent ();
            //attractionImage.HeightRequest = Content.Height * 3 / 4;
            //attractionImage.WidthRequest = Content.Width;
            gc = GameController.getInstance();
            this.attraction = gc.currentTrip.GetCurrentAttraction();
            //attractionName.Text = this.attraction.name;
            string mainPictureUrl = this.attraction.GetMainPictureUrl();
            //attractionImage.Source = ImageSource.FromStream(
            //() => new MemoryStream(Convert.FromBase64String(mainPictureUrl)));
            //attractionImage.Source = mainPictureUrl;
            //attractionImage.IsVisible = !mainPictureUrl.Equals("");
            //watchAgainButton.IsVisible = !this.attraction.GetARURL().Equals("");
            entertainment = gc.currentTrip.GetCurrentAttraction().entertainment;
            //if (entertainment != null)
            //    missionButton.Text = entertainment.EntertainmentName();
            if (entertainment == null){
                missionButton.IsVisible = false;
                or.IsVisible = false;
            }
            //informationButton.Source = ServerConection.URL_MEDIA + "information.png";
            subtitles.Source = ServerConection.URL_MEDIA + "subtitles.jpg";
            info.Source = ServerConection.URL_MEDIA + "info.jpg";
            playVideo.Source = ServerConection.URL_MEDIA + "playVideo.jpg";
            mapBtn.Source = ServerConection.URL_MEDIA + "map.png";
            isFirstAppear = true;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();

            //pop up video on arrival
            if (attraction.videosURLS.Count > 0 && isFirstAppear)
                Navigation.PushModalAsync(new ShowVideoAndTextPage(attraction.videosURLS[0], true));

            missionButton.IsVisible = entertainment != null && !gc.isAttractionDone;
            questionButton.IsVisible = !gc.isAttractionDone;
            or.IsVisible = !gc.isAttractionDone &&  entertainment != null;
            continueButton.IsVisible = gc.isAttractionDone;
            if (gc.isAttractionDone)
                title.Text = AppResources.missionComplete;
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            if (isFirstAppear){
                DependencyService.Get<IAudioService>().PlayAudioFile("TaDa.mp3");
                isFirstAppear = false;
            }
        }

        private async void Information_Button_Clicked(object sender, EventArgs e)
        {
            Lock();
            await Navigation.PushModalAsync(new informationPage(this.attraction));
            UnLock();
        }

        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            Lock();
            await Navigation.PushModalAsync(gc.currentTrip.GetCurrentAttraction().entertainment.EntertainmentPageInstance(attraction));
            UnLock();
        }

        private void Watch_Again_Button_Clicked(object sender, EventArgs e)
        {
            //TODO
        }

        private void Continue_Button_Clicked(object sender, EventArgs e)
        {
            Lock();
            gc.isAttractionDone = false;
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
                Navigation.RemovePage(page);
            if (gc.isFinishTrip)
               Application.Current.MainPage = new FinishTrackPage(gc.CanContinueToLongerTrack());
            else
                Application.Current.MainPage = new NavigationPage();
            UnLock();
        }

        private async void QuestionButton_Clicked(object sender, EventArgs e)
        {
            Lock();
            await Navigation.PushModalAsync(new MultipleChoiceQuestionPage(attraction));
            UnLock();
        }

        private async void PlayVideo_Clicked(object sender, EventArgs e)
        {
            if (attraction.videosURLS.Count > 0)
            {
                Lock();
                await Navigation.PushModalAsync(new ShowVideoAndTextPage(attraction.videosURLS[0], true));
                UnLock();
            }
        }

        private async void MapBtn_Clicked(object sender, EventArgs e)
        {
            Lock();
            //added with map as static field
            await Navigation.PushModalAsync(NavigationPage.myMap);
            UnLock();
        }

        private async void Subtitles_Clicked(object sender, EventArgs e)
        {
            Lock();
            await Navigation.PushModalAsync(new ShowVideoAndTextPage("", false));
            UnLock();
        }


        private void Lock()
        {
            ButtonsLocker.LockAll(btnLayout);
            subtitles.IsEnabled = false;
            info.IsEnabled = false;
            playVideo.IsEnabled = false;
            mapBtn.IsEnabled = false;
        }

        private void UnLock()
        {
            ButtonsLocker.UnlockAll(btnLayout);
            subtitles.IsEnabled = true;
            info.IsEnabled = true;
            playVideo.IsEnabled = true;
            mapBtn.IsEnabled = true;
        }

        protected override bool OnBackButtonPressed()
        {
            //return base.OnBackButtonPressed();

            return true;
        }
    }
}

//to lock:
//btnLayout-mission, question, continue
//subtitles, info, playVideo
//mapBtn