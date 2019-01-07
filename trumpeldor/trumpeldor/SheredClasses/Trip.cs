using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Trip
    {
        internal int id { get; set; }
        internal User user { get; set; }
        internal string groupName { get; set; }
        internal List<int> playersAges { get; set; }
        internal int score { get; set; }
        internal Track track { get; set; }  //TODO: need to think how we wont save so much information in the user's phone
        //internal Attraction nextAttraction { get; set; }
        internal List<Attraction> attractionsDone { get; set; } //TODO: need to think how we wont save so much information in the user's phone

        public Trip()
        {
        }

        internal void DoneMyAttraction(Attraction nextAttraction)
        {
            attractionsDone.Add(nextAttraction);
        }

        internal Attraction GetCurrentAttraction()
        {
            return attractionsDone[attractionsDone.Count - 1];
        }
    }
}
