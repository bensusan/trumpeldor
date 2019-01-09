using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Trip
    {
        public int id { get; set; }
        public User user { get; set; }
        public string groupName { get; set; }
        public List<int> playersAges { get; set; }
        public int score { get; set; }
        public Track track { get; set; }
        public List<Attraction> attractionsDone { get; set; }
        public List<FeedbackInstance> feedbacks { get; set; }

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
