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
	public partial class HintPage : ContentPage
	{
        private double lat=0, lon=0;
		public HintPage (string hintStr)
		{
			InitializeComponent ();
            
            if (hintStr.Contains("http://132.72.23.64:12345/media/"))
            {
                try
                {
                    webView.Source = hintStr;
                    /*WebView wv = new WebView();
                    wv.WidthRequest = 1000;
                    wv.HeightRequest = 1000;
                    wv.Source = hintStr;*/
                }
                catch(Exception e)
                {
                    Alert(e.Message);
                }
                
            }
            else
            {
                generalInformation.Text = hintStr;
            }
            /*else if (hintStr.Contains(','))
            {
                CallToMapPage(hintStr);
                
            }*/

            
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