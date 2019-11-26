const functions = require('firebase-functions');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//

exports.helloWorld = functions.https.onRequest((request, response) => {
    response.send("Hello from DevHack!");
});

exports.newregistry = functions
    .firestore
    .document('registries/{registry}')
    .onCreate((snap, context) => {
        return console.log(snap.data());
    });
