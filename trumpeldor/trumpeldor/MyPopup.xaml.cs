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
        public string currUrl = "";
		public MyPopup (string url)
		{
			InitializeComponent ();
            currUrl = url;
            webView.Source = currUrl;
        }

        void Handle_Clicked(object sender, System.EventArgs e)
        {
            PopupNavigation.Instance.PopAsync(true);
        }
	}
}