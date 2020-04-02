'use strict';

const _ = require('lodash');
const chai = require('chai');

const testModule = require('./rearrange_even_odd');

const expect = chai.expect;

describe('Testing rearrange_even_odd.js', function () {
    context('Testing solution()', function () {
        const tests = {
            1: {
                input: [7, 7, 4, 0, 9, 8, 2, 4, 1, 9],
                expectedResult: [4, 2, 4, 0, 8, 9, 7, 7, 1, 9]
            }
        };

        _.map(tests, function (testCase, caseNumber) {
            it(`CASE ${caseNumber}`, function () {
                const result = testModule.solution(testCase.input);

                expect(result).to.be.eql(testCase.expectedResult);
            });
        });
    });

    context('Testing isEven()', function () {
        const tests = {
            1: {
                input: 42,
                expectedResult: true
            },
            2: {
                input: 21,
                expectedResult: false
            },
            3: {
                input: -1,
                expectedResult: false
            },
            4: {
                input: -2,
                expectedResult: true
            },
            5: {
                input: 0,
                expectedResult: true
            }
        };

        _.map(tests, function (testCase, caseNumber) {
            it(`CASE ${caseNumber}`, function () {
                const result = testModule.isEven(testCase.input);

                expect(result).to.be.eql(testCase.expectedResult);
            });
        });
    });

    context('Testing isOdd()', function () {
        const tests = {
            1: {
                input: 42,
                expectedResult: false
            },
            2: {
                input: 21,
                expectedResult: true
            },
            3: {
                input: -1,
                expectedResult: true
            },
            4: {
                input: -2,
                expectedResult: false
            },
            5: {
                input: 0,
                expectedResult: false
            }
        };

        _.map(tests, function (testCase, caseNumber) {
            it(`CASE ${caseNumber}`, function () {
                const result = testModule.isOdd(testCase.input);

                expect(result).to.be.eql(testCase.expectedResult);
            });
        });
    });
});
