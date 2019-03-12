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
        }

        public AttractionPage(Attraction attraction)
        {
            InitializeComponent();
            this.attraction = attraction;
            attractionName.Text = attraction.name;
            string mainPictureUrl = attraction.GetMainPictureUrl();
            attractionImage.Source = mainPictureUrl;
            attractionImage.IsVisible = !mainPictureUrl.Equals("");
            watchAgainButton.IsVisible = !this.attraction.GetARURL().Equals("");
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            DependencyService.Get<IAudioService>().PlayAudioFile("TaDa.mp3");
        }

        private async void Information_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage(this.attraction.description));
        }
        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new SlidingPuzzlePage());
        }
        private async void Question_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MultipleChoiceQuestionPage(attraction.americanQuestion));
        }
        private void Watch_Again_Button_Clicked(object sender, EventArgs e)
        {
            //TODO
        }
    }
}