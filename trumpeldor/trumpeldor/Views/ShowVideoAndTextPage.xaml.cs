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
	public partial class ShowVideoAndTextPage : ContentPage
	{
        public string currTxt = "";
        public ShowVideoAndTextPage (string txt, bool isUrl)
		{
            InitializeComponent();
            removeButton.Source = ServerConection.URL_MEDIA + "delete.png";
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
            Navigation.PopModalAsync();
        }
    }
}