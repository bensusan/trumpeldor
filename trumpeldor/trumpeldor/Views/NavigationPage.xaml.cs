﻿using System;
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
            //((App)(Application.Current)).getGameController().currentTrip.GetCurrentAttraction()-for the hint
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().GetScore();
            //mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            mapImage.Text = "map";
            SheredClasses.Clue nextClue = ((App)(Application.Current)).getGameController().GetFisrtHint();
            nextClue.addToLayout(hintsLayout);
        }

        private void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
            SheredClasses.Clue nextHint=((App)(Application.Current)).getGameController().GetHint();
            nextHint.addToLayout(hintsLayout);
            scoreLabel.Text = "score: " + ((App)(Application.Current)).getGameController().GetScore(); 
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            DisplayAlert("success", "You've Reached Your Destionation", "OK");
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new TrackPointPage();
        }

        private async void mapImage_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MapPage());
        }
    }
}