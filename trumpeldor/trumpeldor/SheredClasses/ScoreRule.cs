using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class ScoreRule
    {
        public string ruleName { get; set; }
        public int score { get; set; }

        public enum Kinds { Hints_More_Than_Three, AQ_Mistake, AQ_Correct, Attraction_Arrive, Sliding_Puzzle_Solved, Taking_Picture_Done, Puzzle_Solved };
        private static string Hints_More_Than_Three_String = "hmtt", AQ_Mistake_String = "aqm", AQ_Correct_String = "aqc", Attraction_Arrive_String = "aa", Sliding_Puzzle_Solved_String = "sps", Taking_Picture_Done_String = "ttd", Puzzle_Solved_String = "ps";

        //public static Dictionary<Kinds, string> kind2String = new Dictionary<Kinds, string>()
        //{
        //    {Kinds.HintPicture, hintPictureKind},
        //    {Kinds.HintText, hintTextKind},
        //    {Kinds.HintVideo, hintVideoKind}
        //};

        public static Dictionary<string, Kinds> string2Kind = new Dictionary<string, Kinds>()
        {
            {Hints_More_Than_Three_String, Kinds.Hints_More_Than_Three},
            {AQ_Mistake_String, Kinds.AQ_Mistake},
            {AQ_Correct_String, Kinds.AQ_Correct },
            {Attraction_Arrive_String, Kinds.Attraction_Arrive },
            {Sliding_Puzzle_Solved_String, Kinds.Sliding_Puzzle_Solved },
            {Taking_Picture_Done_String, Kinds.Taking_Picture_Done },
            {Puzzle_Solved_String, Kinds.Puzzle_Solved }
        };

        public Kinds GetKind()
        {
            return string2Kind[ruleName];
        }

    }
}
