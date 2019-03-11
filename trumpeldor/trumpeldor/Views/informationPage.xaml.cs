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
	public partial class informationPage : ContentPage
	{
        GameController gc;
		public informationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            generalInformation.Text = gc.GetGeneralInformation();
        }

        public informationPage(string information) : this()
        {
            generalInformation.Text = information;
        }
    }
}