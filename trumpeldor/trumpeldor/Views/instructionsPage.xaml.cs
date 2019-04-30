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
		public instructionsPage ()
		{
            InitializeComponent ();
        }

        public instructionsPage(Entertainment entertainment)
        {
            InitializeComponent();
            details.Text = entertainment.description;
        }

    }
}