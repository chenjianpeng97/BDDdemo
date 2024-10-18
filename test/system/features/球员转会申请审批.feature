# Created by Administrator at 2024/10/16
Feature: 球员的转会申请单据可以被决策者审批
  # Enter feature description here
  AS 总经理
  I WANT 审批球员的转会申请单据
  SO THAT 对球员转会的俱乐部进行控制
  Scenario: 球员的转会申请被审批通过
    # Enter steps here
    Given 球员提交转会申请
    When 总经理填写审批意见
    And 总经理同意球员转会申请
    Then 球员提交的转会申请状态为"审批通过"
    And 球员可见审批意见
  Scenario: 球员的转会申请被审批拒绝
    # Enter steps here
    Given 球员提交转会申请
    When 总经理填写审批意见
    And 总经理拒绝球员转会申请
    Then 球员提交的转会申请状态为"审批拒绝"
    And 球员可见审批意见
#  Scenario: 球员的转会申请审批超时