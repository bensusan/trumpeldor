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
            w.Source = "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/y.png";
            //w.Source = "https://www.xamarin.com/content/images/pages/forms/example-app.png";
        }
	}
}