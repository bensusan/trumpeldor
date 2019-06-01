using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Setttings
    {
        public List<Point> boundaries { get; set; }
        public string logo { get; set; }
        public int loginHours { get; set; }
        public List<ScoreRule> scoreRules { get; set; }
    }
}
