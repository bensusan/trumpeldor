using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class instructionsPage : ContentPage
	{
        private GameController gc;
		public instructionsPage ()
		{
            InitializeComponent ();
            gc = GameController.getInstance();
            if (gc.appInformationAndInstruction != null)
                details.Text = gc.GetCurrentLanguageText(gc.appInformationAndInstruction.how_to_play);
        }

        public instructionsPage(Entertainment entertainment)
        {
            InitializeComponent();
            gc = GameController.getInstance();
            details.Text = gc.GetCurrentLanguageText(entertainment.description);
        }

    }
}