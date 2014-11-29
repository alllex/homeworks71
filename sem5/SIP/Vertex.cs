using System;

namespace SIP
{
	public class Vertex
	{
		static int counter = 0;
		int identifier = counter++;

		public Vertex(int id, String lbl)
		{
			this.ID = id;
			this.Label = lbl; 
		}

		public int ID { get; private set; }
		public String Label { get; private set; }
		
		public int CompareTo(object obj)
		{
			if (obj == null) return 1;
			var other = obj as Vertex;
			if (other != null) return this.Equals (other) ? 0 : 1;
			throw new ArgumentException ("Object is not an Vertex");
		}

		public override bool Equals(object obj)
		{
			if (obj == null) return false;
			var other = obj as Vertex;
			if (other != null) return this.identifier == other.identifier;
			throw new ArgumentException ("Object is not an Vertex");
		}

		public override int GetHashCode()
		{
			return identifier ^ (Label.GetHashCode () & ID.GetHashCode ()) ^ 37;
		}
	}
}
