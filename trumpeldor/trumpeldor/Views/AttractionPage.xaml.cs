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
	public partial class AttractionPage : ContentPage
	{
        private GameController gc = ((App)(Application.Current)).getGameController();
        public AttractionPage()
		{
			InitializeComponent ();
            scoreLabel.Text = AppResources.score +": " + gc.currentTrip.score;
            attractionName.Text = gc.currentTrip.GetCurrentAttraction().name;
            string mainPictureUrl = gc.GetCurrentAttractionImage();
            attractionImage.Source = mainPictureUrl;

            attractionImage.IsVisible = !mainPictureUrl.Equals("");
            watchAgainButton.IsVisible = gc.IsCurrentAttractionHasAR();
        }

        private async void Information_Button_Clicked(object sender, EventArgs e)
        {
            //await Navigation.PushModalAsync(new AttractionInformationPage());
        }
        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            //await Navigation.PushModalAsync(new MissionPage());
        }
        private async void Question_Button_Clicked(object sender, EventArgs e)
        {
            //await Navigation.PushModalAsync(new MultipleChoiceQuestionPage());
        }
        private void Watch_Again_Button_Clicked(object sender, EventArgs e)
        {
            //TODO
        }
    }
}