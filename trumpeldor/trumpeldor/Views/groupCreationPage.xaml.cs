using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class groupCreationPage : ContentPage
    {
        
        private GameController.pathLength selectedPathLength;

        public groupCreationPage()
        {
            InitializeComponent();
        }

        private void Select_Short_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            selectedPathLength = GameController.pathLength.shortPath;
        }
        private void Select_Medium_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            selectedPathLength = GameController.pathLength.mediumPath;
        }
        private void Select_Long_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            selectedPathLength = GameController.pathLength.longPath;
        }

        private void Select_Path_Button_Clicked(object sender, EventArgs e)
        {
            StartGameButton.IsEnabled = true;
            int count = lengthButtonGroup.Children.Count;
            View v = null;
            for (int i = 0; i < count; i++)
            {
                v = lengthButtonGroup.Children.ElementAt(i);
                v.IsEnabled = true;
            }
            ((Button)sender).IsEnabled = false;
        }
        
        private void Add_Player_Button_Clicked(object sender, EventArgs e)
        {
            
            int nextRow = agesGrid.RowDefinitions.Count;
            agesGrid.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            agesGrid.Children.Add(new Label { Text = nextRow + ")" }, 0, nextRow);
            agesGrid.Children.Add(new Entry { Keyboard=Keyboard.Numeric }, 1, nextRow);

        }
        private void Start_Game_Button_Clicked(object sender, EventArgs e)
        {
            List<int> agesList = new List<int>();
            foreach(View child in agesGrid.Children)
            {
                if(child is Entry)
                {
                    agesList.Add(Int32.Parse(((Entry)child).Text));
                }
            }
            String groupName=groupNameEntry.Text;

            ((App)(Application.Current)).getGameController().createGroup(groupName,agesList);
            ((App)(Application.Current)).getGameController().selectPath(selectedPathLength);
            ((App)(Application.Current)).getGameController().selectNextTrackPoint();

            Application.Current.MainPage = new NavigationPage();
        }
    }
}