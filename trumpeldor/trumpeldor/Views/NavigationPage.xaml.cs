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
	public partial class NavigationPage : ContentPage
	{
		public NavigationPage ()
		{
			InitializeComponent ();
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().getScore();
            mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
		}

        private void Get_Clue_Button_Clicked(object sender, EventArgs e)
        {
            SheredClasses.Clue nextClue=((App)(Application.Current)).getGameController().getClue();
            nextClue.addToLayout(cluesLayout);
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().getScore();
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            DisplayAlert("success", "You've Reached Your Destionation", "OK");
            Application.Current.MainPage = new TrackPointPage();
        }
    }
}