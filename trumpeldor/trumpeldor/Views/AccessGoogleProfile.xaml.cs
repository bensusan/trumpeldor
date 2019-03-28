using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class AccessGoogleProfile : ContentPage
	{
        string clientIdAndroid = "416426124345-igghe7dik01k4e6jrgtmikpevjm3auvm.apps.googleusercontent.com";
        string clientIdIOS = "416426124345-fr7pa2p2s8tcnc9mtkipcm49950vtm1m.apps.googleusercontent.com";

        public AccessGoogleProfile ()
		{
			InitializeComponent ();
		}
	}
}