//
//  ContentView.swift
//  TreatFinder
//
//  Created by Aishwarya Sudarshan on 10/22/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("TreatFinder")
            TabView(selection: /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Selection@*/.constant(1)/*@END_MENU_TOKEN@*/) {
                Text("Insert Map once Finished").tabItem { Text("Live Map") }.tag(1)
                Text("Insert Rating Cards").tabItem { Text("Rating") }.tag(2)
            }
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
