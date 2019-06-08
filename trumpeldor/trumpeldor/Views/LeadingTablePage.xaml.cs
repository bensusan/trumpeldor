using Plugin.Multilingual;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class LeadingTablePage : ContentPage
	{
        GameController gc;
		public LeadingTablePage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            if (CrossMultilingual.Current.CurrentCultureInfo.Equals(gc.hebrew))
            {
                leadingTable.FlowDirection = FlowDirection.RightToLeft;
                userPlace.FlowDirection = FlowDirection.RightToLeft;
            }
            //scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            List<UserGroupScore> leadingTableData = gc.GetLeadingTable();
            int userPlaceIndex = -1;
            for (int i=0; i< leadingTableData.Count; i++)
            {
                Color c = Color.White;
                if (leadingTableData[i].groupName.Equals(gc.currentTrip.groupName) && leadingTableData[i].score == gc.GetScore()){
                    c = Color.Orange;
                    userPlaceIndex = i;
                }
                leadingTable.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
                Label lblPosition = new Label { Text = (i+1) + "", HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = c, Margin = 0 };
                lblPosition.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sPosition = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = c};
                sPosition.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sPosition.Children.Add(lblPosition);
                leadingTable.Children.Add(sPosition, 0, i+1);
                Label lblGroupName = new Label { Text = leadingTableData[i].groupName, HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = c, Margin = 0 };
                lblGroupName.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sGroupName = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = c };
                sGroupName.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sGroupName.Children.Add(lblGroupName);
                leadingTable.Children.Add(sGroupName, 1, i+1);
                Label lblScore = new Label { Text = "" + leadingTableData[i].score, HorizontalOptions=LayoutOptions.CenterAndExpand, BackgroundColor = c, Margin = 0 };
                lblScore.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sScore = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = c };
                sScore.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sScore.Children.Add(lblScore);
                leadingTable.Children.Add(sScore, 2, i+1);
            }
            if(userPlaceIndex != -1)
            {
                userPlace.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
                Label lblPosition = new Label { Text = (userPlaceIndex + 1) + "", HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = Color.Orange, Margin = 0 };
                lblPosition.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sPosition = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = Color.Orange };
                sPosition.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sPosition.Children.Add(lblPosition);
                userPlace.Children.Add(sPosition, 0, 0);
                Label lblGroupName = new Label { Text = leadingTableData[userPlaceIndex].groupName, HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = Color.Orange, Margin = 0 };
                lblGroupName.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sGroupName = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = Color.Orange };
                sGroupName.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sGroupName.Children.Add(lblGroupName);
                userPlace.Children.Add(sGroupName, 1, 0);
                Label lblScore = new Label { Text = "" + leadingTableData[userPlaceIndex].score, HorizontalOptions = LayoutOptions.CenterAndExpand, BackgroundColor = Color.Orange, Margin=0};
                lblScore.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                StackLayout sScore = new StackLayout { HorizontalOptions = LayoutOptions.Fill, VerticalOptions = LayoutOptions.Fill, BackgroundColor = Color.Orange };
                sScore.SetDynamicResource(VisualElement.StyleProperty, "mainStackLayout");
                sScore.Children.Add(lblScore);
                userPlace.Children.Add(sScore, 2, 0);
                userPlace.IsVisible = true;
            }
        }

        
	}
}