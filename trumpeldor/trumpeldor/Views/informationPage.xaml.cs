﻿using System;
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
		public informationPage ()
		{
			InitializeComponent ();
            generalInformation.Text = ((App)Application.Current).getGameController().GetGeneralInformation();
        }

        public informationPage(string information)
        {
            InitializeComponent();
            generalInformation.Text = information;
        }
    }
}