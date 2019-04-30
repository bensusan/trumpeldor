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
	public partial class MissionPage : ContentPage
	{
        private GameController gc;
        private ContentPage attractionPage;
		public MissionPage (ContentPage attractionPage)
		{
			InitializeComponent ();
            this.attractionPage = attractionPage;
            gc = GameController.getInstance();
            missionButton.Text = gc.currentTrip.GetCurrentAttraction().entertainment.EntertainmentName();
		}

        protected override void OnAppearing()
        {
            if (gc.isAttractionDone)
                Device.BeginInvokeOnMainThread(async () => await Navigation.PopModalAsync());
            base.OnAppearing();
        }

        private async void Question_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MultipleChoiceQuestionPage());
        }

        private async void Mission_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(gc.currentTrip.GetCurrentAttraction().entertainment.EntertainmentPageInstance());
        }
    }
}