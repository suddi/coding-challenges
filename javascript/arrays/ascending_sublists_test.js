'use strict';

const _ = require('lodash');
const chai = require('chai');

const testModule = require('./ascending_sublists');

const expect = chai.expect;

describe('Testing ascending_sublists.js', function () {
    context('Testing solution()', function () {
        const tests = {
            1: {
                input: [1, 2, 10, 10, 8, 12, 5, 23, 1],
                expectedResult: [[1, 2, 10, 10], [8, 12], [5, 23], [1]]
            },
            2: {
                input: [3, 4, 5, 12, 2, 3, 5, 2, 5, -1],
                expectedResult: [[3, 4, 5, 12], [2, 3, 5], [2, 5], [-1]]
            },
            3: {
                input: [1, 2, 3],
                expectedResult: [[1, 2, 3]]
            },
            4: {
                input: [],
                expectedResult: []
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
