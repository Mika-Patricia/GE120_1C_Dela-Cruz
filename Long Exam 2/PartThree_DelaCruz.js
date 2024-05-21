
import React from 'react';//to create a state
import { Image } from 'react-native';//import from react native
import { Picker } from '@react-native-picker/picker';//import from react native
import { StatusBar } from 'expo-status-bar';//import from react native
import { StyleSheet, Text, TextInput, View, Button } from 'react-native'; //components
import jett from './jett.jpg' ;

export default function App() {

  const [outputValue, setOutputValue] = React.useState('---');  //INITIALIZATION
  const [inputValue, setInputValue] = React.useState('Input value here..'); //INITIALIZATION
  const [inputCase, setInputCase] = React.useState("Select Case"); //INITIALIZATION
  const blurhash =
  '|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj['; //INITIALIZATION

  function convertobearing(value) {  //function
      /*
      Compute for the numerical values in converting azimuth to bearing.*/

        
      if (inputCase == "2") {
        var degrees = Math.floor(value)
        var minutes = Math.floor((value-degrees)*60)
        var seconds = Math.round((value-degrees-(minutes/60))*3600)

        var output = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString())

        setOutputValue(output)
      }
      if (inputCase == "1"){
        var elements = value.split("-")
        var output = parseFloat(elements[0]) + parseFloat(elements[1])/60 + parseFloat(elements [2])/3600
        setOutputValue(output)
      }
  }
/* sets direction of the DMS after getting the numerical value */
  function direction(output){

    if (output > 0 && output < 90); {
        setbearing(direction) = 'S {: ^5} W' .format (round(output,3))
 } if (output > 90 && output < 180); {
        setbearing(direction) = 'N {: ^5} W' .format (round(180 - output,3))
} if (output > 180 && output < 270); {setbearing(direction) = 'N {: ^5} E' .format (round(output - 180,3))
    } if (output > 270 && output < 360);{
    setbearing(direction) = 'S {: ^5} E' .format (round(360 - output,3))
    } 
    if (output === 0){
      setbearing(direction) = "Due South"}
      if (output === 90) {
     setbearing(direction) = "Due West"}
    if (output === 180){
      setbearing(direction) = "Due North"}
    if (output === 270){
            setbearing(direction) = "Due East"}
    else {
    setbearing(direction) = "UNKNOWN"}

  }
  return (
    <View style={styles.box}>
      <View style={styles.box1}>
        <Text style={styles.titleText}> WELCOME output (DMS) to Bearing (DMS) </Text>
      </View>
      
      <View style={styles.box2}> 
        <View style={styles.box21}>
          <Text>Input Case</Text>
          <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="output to Bearing" values="1" />
          </Picker>
        </View>
      
        <View style={styles.box22}>
          <TextInput
            style={styles.input}
            onChangeText={setInputValue}
            value={inputValue}
          />
          <Button
            title="Convert"
            onPress={() => converttobearing(inputValue)}
          />
        </View>  
      </View>

      <View style={styles.box3}>
        <Text style={styles.titleText}> Output: </Text>
        <Text style={styles.titleText}> {outputValue} </Text>
      </View>
        
      <View style={styles.box4}>
        <Image
          style={styles.image}
          source={jett}
          placeholder={blurhash}
          contentFit="cover"
          transition={1000}
        />
      </View>
    </View>
  );
}

//INITIALIZATION
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  box1: {
    width: '100%', 
    height: '10%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  box2: {
    width: '100%', 
    height: '25%', 
    alignItems: 'center', 
    justifyContent: 'center',      
    padding: 10  
  },
  box21: {
    flexDirection: 'column',
    width: '100%',
    height: '50%',   
    padding: 10
  },
  box22: {
    flex: 1,
    width: '100%',
    height: '50%',
  },
  box3: {
    width: '100%', 
    height: '25%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  box4: {
    width: '100%', 
    height: '40%', 
    alignItems: 'center', 
    justifyContent: 'center'        
  },
  titleText: {
    fontSize: 24,
    fontWeight: 'bold', 
    color: 'black'
  },
  image: {
    flex: 1,
    width: '100%',
    backgroundColor: 'pink',
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black'
  }
});

/* THE LAYOUT

The title will be on top, followed by the text field to type the given Azimuth by the user. Then 
just below it is the button that can be pressed which converts the input azimuth into bearing in DMS. 
And most importantly, the text that shows the Output. And for the negative space left, a picture would
be nice to place. But since we are not allowed to access the internet, I will only put the code as if
there is an image indeed.*/