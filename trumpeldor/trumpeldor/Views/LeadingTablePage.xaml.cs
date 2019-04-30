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
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            List<UserGroupScore> leadingTableData = gc.GetLeadingTable();
            for(int i=0; i< leadingTableData.Count; i++)
            {
                leadingTable.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
                Label lblPosition = new Label { Text = (i+1) + ")"};
                lblPosition.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                leadingTable.Children.Add(lblPosition, 0, i+1);
                Label lblGroupName = new Label { Text = leadingTableData[i].groupName, HorizontalOptions = LayoutOptions.Center };
                lblGroupName.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                leadingTable.Children.Add(lblGroupName, 1, i+1);
                Label lblScore = new Label { Text = "" + leadingTableData[i].score, HorizontalOptions=LayoutOptions.Center};
                lblScore.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
                leadingTable.Children.Add(lblScore, 2, i+1);
            }
        }
	}
}