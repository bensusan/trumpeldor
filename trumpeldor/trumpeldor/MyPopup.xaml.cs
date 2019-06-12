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
        public string currTxt = "";
		public MyPopup (string txt, bool isUrl)
		{
			InitializeComponent ();
            currTxt = txt;
            if (isUrl)
            {
                webView.Source = currTxt;
            }
            else
            {
                textLbl.Text = txt;
            }
        }

        void Handle_Clicked(object sender, System.EventArgs e)
        {
            PopupNavigation.Instance.PopAsync(true);
        }
	}
}