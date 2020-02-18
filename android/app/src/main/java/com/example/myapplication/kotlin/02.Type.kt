package com.example.myapplication.kotlin

// 02. 자료형
// 정수형 -> long > Int > Short > Byte
// 실수형 -> Double > Float
// 문자 -> Char
// 문자열 -> String
// 논리형(True / False) -> Boolean

//변수 선언하는 방법(1)
//Variable/Value 변수명 = 값
//var/val 변수명 = 값
var number = 10

//변수 선언하는 방법(2)
//var/val 변수 : 자료형 = 값
var number1:  Int = 20
var hello1 : String = "Hello"
var point1 : Double = 3.4

//val로 할지 var로 할지 모르겠다?
//1. 절대 변하지 않는 값이라면 당연히 value
//2. 값이 변한다면 당연히 variable
//3. 변할지 안변할지 모르겠다면 일단은 value. 혹시 변하면 나중가서 바꾸면됨. 원래 무슨값이었는지 알 수 있음.

fun main(array: Array<String>){
    number = 20
    //number = 20.5
}