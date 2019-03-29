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
            List<UserGroupScore> leadingTableData = gc.GetLeadingTable();
            for(int i=0; i< leadingTableData.Count; i++)
            {
                leadingTable.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
                Label lblPosition = new Label { Text = (i+1) + ")" };
                lblPosition.SetDynamicResource(VisualElement.StyleProperty, "lableStyle");
                leadingTable.Children.Add(lblPosition, 0, i+1);
                Label lblGroupName = new Label { Text = leadingTableData[i].groupName };
                lblGroupName.SetDynamicResource(VisualElement.StyleProperty, "lableStyle");
                leadingTable.Children.Add(lblGroupName, 1, i+1);
                Label lblScore = new Label { Text = "" + leadingTableData[i].score };
                lblScore.SetDynamicResource(VisualElement.StyleProperty, "lableStyle");
                leadingTable.Children.Add(lblScore, 2, i+1);
            }
        }
	}
}