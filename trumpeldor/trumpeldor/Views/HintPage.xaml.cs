using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class HintPage : ContentPage
	{
        private double lat=0, lon=0;
		public HintPage (Hint hint)
		{
			InitializeComponent ();
            string hintStr = hint.kind;
            string urlPref = "http://132.72.23.64:12345/media/";
            if (hintStr.Equals( "HP" ) || hintStr=="HV")//case picture or video
            {
                webView.IsVisible = true;
                string tmp = hint.data.Substring(2, hint.data.Length - 4);
                try
                {
                    webView.Source = urlPref + tmp/*hint.data*/;
                }
                catch(Exception e)
                {
                    Alert(e.Message);
                }
            
            }
            else //case text
            {
                webView.IsVisible = false;
                textualHint.Text = hint.data;
            }
		}

        private async void Alert(string s)
        {
            await DisplayAlert("error", s, "ok");
        }
        private async void CallToMapPage(string hintStr)
        {
            char[] seperate = new char[] { ',', ' ' };
            string[] coordinates = new string[2];
            if (hintStr.Split(seperate).Length == coordinates.Length)
            {
                coordinates = hintStr.Split(seperate);
                try
                {
                    lat = Convert.ToDouble(coordinates[0]);
                    lon = Convert.ToDouble(coordinates[1]);
                    Point p = new Point(lat, lon);
                    await DisplayAlert("final hint", "click ok to view the next point on the map", "ok");
                        //.ContinueWith((a) =>
                   // Application.Current.MainPage = new MapPage(p));
                }
                catch (Exception e)
                {
                    await DisplayAlert("error", e.Message, "close");
                }
            }
        }
    }
}