using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Hint
    {
        
        public int id { get; set; }
        public string kind { get; set; }
        public string data { get; set; }
        public string description { get; set; }

        //not for use
        public enum Kinds { HintPicture, HintText, HintVideo };
        private static string hintPictureKind = "HP", hintTextKind = "HT", hintVideoKind = "HV";

        public static Dictionary<Kinds, string> kind2String = new Dictionary<Kinds, string>()
        {
            {Kinds.HintPicture, hintPictureKind},
            {Kinds.HintText, hintTextKind},
            {Kinds.HintVideo, hintVideoKind}
        };

        public static Dictionary<string, Kinds> string2Kind = new Dictionary<string, Kinds>()
        {
            {hintPictureKind, Kinds.HintPicture},
            {hintTextKind, Kinds.HintText},
            {hintVideoKind, Kinds.HintVideo }
        };

        public Kinds GetKindHint() {
            return string2Kind[kind];
        }
    }
}
