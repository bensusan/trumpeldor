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
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().GetScore();
            //mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            mapImage.Text = "map";
            SheredClasses.Clue nextClue = ((App)(Application.Current)).getGameController().GetFisrtHint();
            nextClue.addToLayout(hintsLayout);
        }

        private void Get_Clue_Button_Clicked(object sender, EventArgs e)
        {
            SheredClasses.Clue nextClue=((App)(Application.Current)).getGameController().GetHint();
            nextClue.addToLayout(hintsLayout);
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().GetScore();
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            DisplayAlert("success", "You've Reached Your Destionation", "OK");
            Application.Current.MainPage = new TrackPointPage();
        }

        private void mapImage_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new MapPage();
        }
    }
}