using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class instructionsPage : ContentPage
	{
		public instructionsPage ()
		{
            InitializeComponent ();
            //w.Source = "http://132.72.234.59:12345/media/y.png";
            w.Source = "https://www.xamarin.com/content/images/pages/forms/example-app.png";
        }

        public async void GetFile(object sender, EventArgs e)
        {
            Stream s = await ((App)(Application.Current)).getGameController().GetFile("x.jpg");

            //img.Source = ImageSource.FromStream(() => s);
            await DisplayAlert("Alert", "finally here", "ok");
        }
	}
}