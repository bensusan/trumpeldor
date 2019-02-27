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
            scoreLabel.Text = AppResources.score + ": " + gc.currentTrip.score;
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
            scoreLabel.Text = AppResources.score + ": -1";
            attractionName.Text = attraction.name;
            string mainPictureUrl = attraction.GetMainPictureUrl();
            attractionImage.Source = mainPictureUrl;
            attractionImage.IsVisible = !mainPictureUrl.Equals("");
            watchAgainButton.IsVisible = !this.attraction.GetARURL().Equals("");
        }

        private async void Information_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage(this.attraction.description));
        }
        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            //await Navigation.PushModalAsync(new MissionPage());
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