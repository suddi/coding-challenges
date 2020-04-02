'use strict';

const _ = require('lodash');
const chai = require('chai');

const testModule = require('./2nd_biggest_number');

const expect = chai.expect;

describe('Testing 2nd_biggest_number.js', function () {
    context('Testing solution()', function () {
        const tests = {
            1: {
                input: [4, 4, -5, 3, 2, 3, 7, 7, 8, 8],
                expectedResult: 7
            },
            2: {
                input: [-1, -2, -15, -1, -2, -1, -2],
                expectedResult: -2
            },
            3: {
                input: [1, 1, 1, 1]
            }
        };

        _.map(tests, function (testCase, caseNumber) {
            it(`CASE ${caseNumber}`, function () {
                const result = testModule.solution(testCase.input);

                expect(result).to.be.eql(testCase.expectedResult);
            });
        });
    });
});
