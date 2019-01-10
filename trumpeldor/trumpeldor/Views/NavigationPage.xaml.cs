﻿using System;
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
	public partial class NavigationPage : ContentPage
	{
        //        gc.currentTrip.GetCurrentAttraction();//-for the hint
        public Attraction nextAttraction;
        public static int hintsIndex = 0;
        Point p = new Point();
        public GameController gc = ((App)Application.Current).getGameController();
        public NavigationPage ()
		{
			InitializeComponent ();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            p.X = nextAttraction.x;
            p.Y = nextAttraction.y;
            //nextAttraction = gc.currentTrip.GetCurrentAttraction();
            scoreLabel.Text = "score: "/* + gc.currentTrip.score*/;
            //mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            mapImage.Text = "map";
            //SheredClasses.Clue nextClue = gc.GetFisrtHint();
            //nextClue.addToLayout(hintsLayout);
        }

        private async void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
            if (nextAttraction != null)
            {
                await Navigation.PushModalAsync(new MapPage(p));
                /* Hint nextHint;
                 nextHint = nextAttraction.hints[hintsIndex];
                 //nextHint.addToLayout(hintsLayout);
                 //scoreLabel.Text = "score: " + gc.currentTrip.score;
                 hintsIndex++;*/
            }

        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            DisplayAlert("success", "You've Reached Your Destionation", "OK");
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new AttractionPage();
        }

        private async void mapImage_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MapPage());
        }
    }
}