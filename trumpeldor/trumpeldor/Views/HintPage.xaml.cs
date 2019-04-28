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
            string urlPref = "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/";

            string hintPictureString;
            Hint.kind2String.TryGetValue(Hint.Kinds.HintPicture, out hintPictureString);
            string hintVideoString;
            Hint.kind2String.TryGetValue(Hint.Kinds.HintVideo, out hintVideoString);
            if(hintStr.Equals(hintPictureString) || hintStr.Equals(hintVideoString)){
                webView.IsVisible = true;
                string tmp = hint.data.Substring(1, hint.data.Length - 2);
                string dt = hint.data;
                webView.Source = urlPref + dt;
            }
            else //case text
            { 
                webView.IsVisible = false;
                textualHint.Text = hint.data;
            }
		}

        //private void Alert(string s)
        //{
        //    Device.BeginInvokeOnMainThread(async () => { await DisplayAlert(AppResources.error, s, AppResources.ok); });
        //}
        //private void CallToMapPage(string hintStr)
        //{
        //    char[] seperate = new char[] { ',', ' ' };
        //    string[] coordinates = new string[2];
        //    if (hintStr.Split(seperate).Length == coordinates.Length)
        //    {
        //        coordinates = hintStr.Split(seperate);
        //        try
        //        {
        //            lat = Convert.ToDouble(coordinates[0]);
        //            lon = Convert.ToDouble(coordinates[1]);
        //            trumpeldor.SheredClasses.Point p = new trumpeldor.SheredClasses.Point(lat, lon);
        //            Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.final_hint, AppResources.click_ok_to_view_the_next_point_on_the_map, AppResources.ok));
        //                //.ContinueWith((a) =>
        //           // Application.Current.MainPage = new MapPage(p));
        //        }
        //        catch (Exception e)
        //        {
        //            Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.error, e.Message, AppResources.close));
        //        }
        //    }
        //}
    }
}