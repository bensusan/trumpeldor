using Rg.Plugins.Popup.Pages;
using Rg.Plugins.Popup.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class MyPopup : PopupPage
    {
        public string url = "https://storage.googleapis.com/appconfig-media/appconfig-content/uploads/2016/04/xamarin-app-logo2.png";
		public MyPopup ()
		{
			InitializeComponent ();
            webView.Source = url;
        }

        void Handle_Clicked(object sender, System.EventArgs e)
        {
            PopupNavigation.Instance.PopAsync(true);
        }
	}
}