using Plugin.Multilingual;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class OpenPage : ContentPage
    {
        public OpenPage()
        {
            InitializeComponent();
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("en");
            Application.Current.MainPage = new FirstPage();
        }

        private void Button_Clicked_1(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("he");
            Application.Current.MainPage = new FirstPage();
        }
    }
}