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
	public partial class MidPage : ContentPage
	{
		public MidPage ()
		{
			InitializeComponent ();
		}

        private void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
            //SheredClasses.Clue nextHint=((App)(Application.Current)).getGameController().GetHint();
            //nextHint.addToLayout(hintsLayout);
            //scoreLabel.Text = "score: " + gc.currentTrip.score; 
        }
    }
}